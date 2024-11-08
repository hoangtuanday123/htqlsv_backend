/* eslint-disable */
/* tslint:disable */
/*
 * ---------------------------------------------------------------
 * ## THIS FILE WAS GENERATED VIA SWAGGER-TYPESCRIPT-API        ##
 * ##                                                           ##
 * ## AUTHOR: acacode                                           ##
 * ## SOURCE: https://github.com/acacode/swagger-typescript-api ##
 * ---------------------------------------------------------------
 */

/** Account */
export interface Account {
  /** Email */
  email: string;
  /** Fullname */
  fullname: string;
  /** Gender */
  gender?: string | null;
  /** Personalid */
  personalID?: string | null;
  /** Phone */
  phone?: string | null;
  /** Address */
  address?: string | null;
  /** Banknumber */
  banknumber?: string | null;
  /** Bankname */
  bankname?: string | null;
  /** Bankbranch */
  bankbranch?: string | null;
  /** Startdate */
  startdate?: string | null;
  /** Hashpassword */
  hashpassword: string;
  /**
   * Createddated
   * @format date-time
   */
  createddated: string;
  /** Createdby */
  Createdby: string;
  /** Role Id */
  role_id: number;
  /** Is Active */
  is_active: boolean;
  /** Major Id */
  major_id?: number | null;
  /** Id */
  id: number;
  /** Role */
  role: string;
  /** Major */
  major?: string | null;
}

/** AccountCreate */
export interface AccountCreate {
  /** Email */
  email: string;
  /** Fullname */
  fullname: string;
  /** Gender */
  gender?: string | null;
  /** Personalid */
  personalID?: string | null;
  /** Phone */
  phone?: string | null;
  /** Address */
  address?: string | null;
  /** Banknumber */
  banknumber?: string | null;
  /** Bankname */
  bankname?: string | null;
  /** Bankbranch */
  bankbranch?: string | null;
  /** Startdate */
  startdate?: string | null;
  /** Hashpassword */
  hashpassword: string;
  /**
   * Createddated
   * @format date-time
   */
  createddated: string;
  /** Createdby */
  Createdby: string;
  /** Role Id */
  role_id: number;
  /** Is Active */
  is_active: boolean;
  /** Major Id */
  major_id?: number | null;
}

/** AccountUpdate */
export interface AccountUpdate {
  /** Email */
  email: string;
  /** Fullname */
  fullname: string;
  /** Gender */
  gender?: string | null;
  /** Personalid */
  personalID?: string | null;
  /** Phone */
  phone?: string | null;
  /** Address */
  address?: string | null;
  /** Banknumber */
  banknumber?: string | null;
  /** Bankname */
  bankname?: string | null;
  /** Bankbranch */
  bankbranch?: string | null;
  /** Startdate */
  startdate?: string | null;
  /** Hashpassword */
  hashpassword: string;
  /**
   * Createddated
   * @format date-time
   */
  createddated: string;
  /** Createdby */
  Createdby: string;
  /** Role Id */
  role_id: number;
  /** Is Active */
  is_active: boolean;
  /** Major Id */
  major_id?: number | null;
  /** Password */
  password: string;
}

/** AuthUser */
export interface AuthUser {
  /** Id */
  id?: string | null;
  /** Email */
  email?: string | null;
  /** Fullname */
  fullname?: string | null;
  /** Role */
  role?: string | null;
}

/** Body_login_auth_login_post */
export interface BodyLoginAuthLoginPost {
  /** Grant Type */
  grant_type?: string | null;
  /** Username */
  username: string;
  /** Password */
  password: string;
  /**
   * Scope
   * @default ""
   */
  scope?: string;
  /** Client Id */
  client_id?: string | null;
  /** Client Secret */
  client_secret?: string | null;
}

/** Classroom */
export interface Classroom {
  /** Name */
  name: string;
  /**
   * Createddated
   * @format date-time
   */
  createddated: string;
  /** Createdby */
  Createdby: string;
  /** Id */
  id: number;
}

/** ClassroomCreate */
export interface ClassroomCreate {
  /** Name */
  name: string;
  /**
   * Createddated
   * @format date-time
   */
  createddated: string;
  /** Createdby */
  Createdby: string;
}

/** ClassroomUpdate */
export interface ClassroomUpdate {
  /** Name */
  name: string;
  /**
   * Createddated
   * @format date-time
   */
  createddated: string;
  /** Createdby */
  Createdby: string;
}

/** Course */
export interface Course {
  /** Name */
  name: string;
  /** Credit */
  credit: number;
  /** Totalprice */
  totalprice: number;
  /**
   * Createddated
   * @format date-time
   */
  createddated: string;
  /** Createdby */
  createdby: string;
  /** Major Id */
  major_id?: number | null;
  /** Id */
  id: number;
  /** Major */
  major?: string | null;
}

/** CourseCreate */
export interface CourseCreate {
  /** Name */
  name: string;
  /** Credit */
  credit: number;
  /** Totalprice */
  totalprice: number;
  /**
   * Createddated
   * @format date-time
   */
  createddated: string;
  /** Createdby */
  createdby: string;
  /** Major Id */
  major_id?: number | null;
}

/** CourseUpdate */
export interface CourseUpdate {
  /** Name */
  name: string;
  /** Credit */
  credit: number;
  /** Totalprice */
  totalprice: number;
  /**
   * Createddated
   * @format date-time
   */
  createddated: string;
  /** Createdby */
  createdby: string;
  /** Major Id */
  major_id?: number | null;
}

/** Department */
export interface Department {
  /** Name */
  name: string;
  /**
   * Createddated
   * @format date-time
   */
  createddated: string;
  /** Createdby */
  createdby: string;
  /** Head Id */
  head_id?: number | null;
  /** Deputy Head Id */
  deputy_head_id?: number | null;
  /** Id */
  id: number;
  /** Head */
  head?: string | null;
  /** Deputy Head */
  deputy_head?: string | null;
}

/** DepartmentCreate */
export interface DepartmentCreate {
  /** Name */
  name: string;
  /**
   * Createddated
   * @format date-time
   */
  createddated: string;
  /** Createdby */
  createdby: string;
  /** Head Id */
  head_id?: number | null;
  /** Deputy Head Id */
  deputy_head_id?: number | null;
}

/** DepartmentUpdate */
export interface DepartmentUpdate {
  /** Name */
  name: string;
  /**
   * Createddated
   * @format date-time
   */
  createddated: string;
  /** Createdby */
  createdby: string;
  /** Head Id */
  head_id?: number | null;
  /** Deputy Head Id */
  deputy_head_id?: number | null;
}

/** Enrollment */
export interface Enrollment {
  /**
   * Createddated
   * @format date-time
   */
  createddated: string;
  /** Createdby */
  createdby: string;
  /** Grade Theory */
  grade_theory: number;
  /** Grade Practice */
  grade_practice: number;
  /** Grade Bonus */
  grade_bonus: number;
  /** Gpa */
  GPA: number;
  /** Status */
  status: string;
  /** Student Id */
  student_id?: number | null;
  /** Open Course Id */
  open_course_id?: number | null;
  /** Id */
  id: number;
  /** Timetheory */
  timetheory?: string | null;
  /** Timepractice */
  timepractice?: string | null;
  /** Student */
  student?: string | null;
  /** Course */
  course?: string | null;
  /** Instructor Theory */
  instructor_theory?: string | null;
  /** Instructor Practice */
  instructor_practice?: string | null;
  /** Semester */
  semester?: string | null;
  /** Classroom */
  classroom?: string | null;
}

/** EnrollmentCreate */
export interface EnrollmentCreate {
  /**
   * Createddated
   * @format date-time
   */
  createddated: string;
  /** Createdby */
  createdby: string;
  /** Grade Theory */
  grade_theory: number;
  /** Grade Practice */
  grade_practice: number;
  /** Grade Bonus */
  grade_bonus: number;
  /** Gpa */
  GPA: number;
  /** Status */
  status: string;
  /** Student Id */
  student_id?: number | null;
  /** Open Course Id */
  open_course_id?: number | null;
}

/** EnrollmentUpdate */
export interface EnrollmentUpdate {
  /**
   * Createddated
   * @format date-time
   */
  createddated: string;
  /** Createdby */
  createdby: string;
  /** Grade Theory */
  grade_theory: number;
  /** Grade Practice */
  grade_practice: number;
  /** Grade Bonus */
  grade_bonus: number;
  /** Gpa */
  GPA: number;
  /** Status */
  status: string;
  /** Student Id */
  student_id?: number | null;
  /** Open Course Id */
  open_course_id?: number | null;
}

/** HTTPValidationError */
export interface HTTPValidationError {
  /** Detail */
  detail?: ValidationError[];
}

/** Major */
export interface Major {
  /** Name */
  name: string;
  /**
   * Createddated
   * @format date-time
   */
  createddated: string;
  /** Createdby */
  createdby: string;
  /** Department Id */
  department_id?: number | null;
  /** Head Id */
  head_id?: number | null;
  /** Deputy Head Id */
  deputy_head_id?: number | null;
  /** Id */
  id: number;
  /** Head */
  head?: string | null;
  /** Deputy Head */
  deputy_head?: string | null;
  /** Department */
  department?: string | null;
}

/** MajorCreate */
export interface MajorCreate {
  /** Name */
  name: string;
  /**
   * Createddated
   * @format date-time
   */
  createddated: string;
  /** Createdby */
  createdby: string;
  /** Department Id */
  department_id?: number | null;
  /** Head Id */
  head_id?: number | null;
  /** Deputy Head Id */
  deputy_head_id?: number | null;
}

/** MajorUpdate */
export interface MajorUpdate {
  /** Name */
  name: string;
  /**
   * Createddated
   * @format date-time
   */
  createddated: string;
  /** Createdby */
  createdby: string;
  /** Department Id */
  department_id?: number | null;
  /** Head Id */
  head_id?: number | null;
  /** Deputy Head Id */
  deputy_head_id?: number | null;
}

/** Opencourse */
export interface Opencourse {
  /**
   * Createddated
   * @format date-time
   */
  createddated: string;
  /** Createdby */
  createdby: string;
  /** Capacity */
  capacity: number;
  /** Timetheory */
  timetheory?: string | null;
  /** Timepractice */
  timepractice?: string | null;
  /** Status */
  status: string;
  /** Is Open */
  is_open: boolean;
  /** Number Of Student */
  number_of_student?: number | null;
  /** Course Id */
  course_id?: number | null;
  /** Instructor Theory Id */
  instructor_theory_id?: number | null;
  /** Instructor Practice Id */
  instructor_practice_id?: number | null;
  /** Semester Id */
  semester_id?: number | null;
  /** Classroom Id */
  classroom_id?: number | null;
  /** Id */
  id: number;
  /** Course */
  course?: string | null;
  /** Instructor Theory */
  instructor_theory?: string | null;
  /** Instructor Practice */
  instructor_practice?: string | null;
  /** Semester */
  semester?: string | null;
  /** Classroom */
  classroom?: string | null;
}

/** OpencourseCreate */
export interface OpencourseCreate {
  /**
   * Createddated
   * @format date-time
   */
  createddated: string;
  /** Createdby */
  createdby: string;
  /** Capacity */
  capacity: number;
  /** Timetheory */
  timetheory?: string | null;
  /** Timepractice */
  timepractice?: string | null;
  /** Status */
  status: string;
  /** Is Open */
  is_open: boolean;
  /** Number Of Student */
  number_of_student?: number | null;
  /** Course Id */
  course_id?: number | null;
  /** Instructor Theory Id */
  instructor_theory_id?: number | null;
  /** Instructor Practice Id */
  instructor_practice_id?: number | null;
  /** Semester Id */
  semester_id?: number | null;
  /** Classroom Id */
  classroom_id?: number | null;
}

/** OpencourseUpdate */
export interface OpencourseUpdate {
  /**
   * Createddated
   * @format date-time
   */
  createddated: string;
  /** Createdby */
  createdby: string;
  /** Capacity */
  capacity: number;
  /** Timetheory */
  timetheory?: string | null;
  /** Timepractice */
  timepractice?: string | null;
  /** Status */
  status: string;
  /** Is Open */
  is_open: boolean;
  /** Number Of Student */
  number_of_student?: number | null;
  /** Course Id */
  course_id?: number | null;
  /** Instructor Theory Id */
  instructor_theory_id?: number | null;
  /** Instructor Practice Id */
  instructor_practice_id?: number | null;
  /** Semester Id */
  semester_id?: number | null;
  /** Classroom Id */
  classroom_id?: number | null;
}

/** Role */
export interface Role {
  /** Rolename */
  rolename: string;
  /** Id */
  id: number;
}

/** Semester */
export interface Semester {
  /** Semester */
  semester: string;
  /**
   * Createddated
   * @format date-time
   */
  createddated: string;
  /** Createdby */
  createdby: string;
  /** Id */
  id: number;
}

/** SemesterCreate */
export interface SemesterCreate {
  /** Semester */
  semester: string;
  /**
   * Createddated
   * @format date-time
   */
  createddated: string;
  /** Createdby */
  createdby: string;
}

/** SemesterUpdate */
export interface SemesterUpdate {
  /** Semester */
  semester: string;
  /**
   * Createddated
   * @format date-time
   */
  createddated: string;
  /** Createdby */
  createdby: string;
}

/** UserSelected */
export interface UserSelected {
  /** Id */
  id: number;
  /** Fullname */
  fullname: string;
}

/** ValidationError */
export interface ValidationError {
  /** Location */
  loc: (string | number)[];
  /** Message */
  msg: string;
  /** Error Type */
  type: string;
}

export type QueryParamsType = Record<string | number, any>;
export type ResponseFormat = keyof Omit<Body, "body" | "bodyUsed">;

export interface FullRequestParams extends Omit<RequestInit, "body"> {
  /** set parameter to `true` for call `securityWorker` for this request */
  secure?: boolean;
  /** request path */
  path: string;
  /** content type of request body */
  type?: ContentType;
  /** query params */
  query?: QueryParamsType;
  /** format of response (i.e. response.json() -> format: "json") */
  format?: ResponseFormat;
  /** request body */
  body?: unknown;
  /** base url */
  baseUrl?: string;
  /** request cancellation token */
  cancelToken?: CancelToken;
}

export type RequestParams = Omit<FullRequestParams, "body" | "method" | "query" | "path">;

export interface ApiConfig<SecurityDataType = unknown> {
  baseUrl?: string;
  baseApiParams?: Omit<RequestParams, "baseUrl" | "cancelToken" | "signal">;
  securityWorker?: (securityData: SecurityDataType | null) => Promise<RequestParams | void> | RequestParams | void;
  customFetch?: typeof fetch;
}

export interface HttpResponse<D extends unknown, E extends unknown = unknown> extends Response {
  data: D;
  error: E;
}

type CancelToken = Symbol | string | number;

export enum ContentType {
  Json = "application/json",
  FormData = "multipart/form-data",
  UrlEncoded = "application/x-www-form-urlencoded",
  Text = "text/plain",
}

export class HttpClient<SecurityDataType = unknown> {
  public baseUrl: string = "";
  private securityData: SecurityDataType | null = null;
  private securityWorker?: ApiConfig<SecurityDataType>["securityWorker"];
  private abortControllers = new Map<CancelToken, AbortController>();
  private customFetch = (...fetchParams: Parameters<typeof fetch>) => fetch(...fetchParams);

  private baseApiParams: RequestParams = {
    credentials: "same-origin",
    headers: {},
    redirect: "follow",
    referrerPolicy: "no-referrer",
  };

  constructor(apiConfig: ApiConfig<SecurityDataType> = {}) {
    Object.assign(this, apiConfig);
  }

  public setSecurityData = (data: SecurityDataType | null) => {
    this.securityData = data;
  };

  protected encodeQueryParam(key: string, value: any) {
    const encodedKey = encodeURIComponent(key);
    return `${encodedKey}=${encodeURIComponent(typeof value === "number" ? value : `${value}`)}`;
  }

  protected addQueryParam(query: QueryParamsType, key: string) {
    return this.encodeQueryParam(key, query[key]);
  }

  protected addArrayQueryParam(query: QueryParamsType, key: string) {
    const value = query[key];
    return value.map((v: any) => this.encodeQueryParam(key, v)).join("&");
  }

  protected toQueryString(rawQuery?: QueryParamsType): string {
    const query = rawQuery || {};
    const keys = Object.keys(query).filter((key) => "undefined" !== typeof query[key]);
    return keys
      .map((key) => (Array.isArray(query[key]) ? this.addArrayQueryParam(query, key) : this.addQueryParam(query, key)))
      .join("&");
  }

  protected addQueryParams(rawQuery?: QueryParamsType): string {
    const queryString = this.toQueryString(rawQuery);
    return queryString ? `?${queryString}` : "";
  }

  private contentFormatters: Record<ContentType, (input: any) => any> = {
    [ContentType.Json]: (input: any) =>
      input !== null && (typeof input === "object" || typeof input === "string") ? JSON.stringify(input) : input,
    [ContentType.Text]: (input: any) => (input !== null && typeof input !== "string" ? JSON.stringify(input) : input),
    [ContentType.FormData]: (input: any) =>
      Object.keys(input || {}).reduce((formData, key) => {
        const property = input[key];
        formData.append(
          key,
          property instanceof Blob
            ? property
            : typeof property === "object" && property !== null
              ? JSON.stringify(property)
              : `${property}`,
        );
        return formData;
      }, new FormData()),
    [ContentType.UrlEncoded]: (input: any) => this.toQueryString(input),
  };

  protected mergeRequestParams(params1: RequestParams, params2?: RequestParams): RequestParams {
    return {
      ...this.baseApiParams,
      ...params1,
      ...(params2 || {}),
      headers: {
        ...(this.baseApiParams.headers || {}),
        ...(params1.headers || {}),
        ...((params2 && params2.headers) || {}),
      },
    };
  }

  protected createAbortSignal = (cancelToken: CancelToken): AbortSignal | undefined => {
    if (this.abortControllers.has(cancelToken)) {
      const abortController = this.abortControllers.get(cancelToken);
      if (abortController) {
        return abortController.signal;
      }
      return void 0;
    }

    const abortController = new AbortController();
    this.abortControllers.set(cancelToken, abortController);
    return abortController.signal;
  };

  public abortRequest = (cancelToken: CancelToken) => {
    const abortController = this.abortControllers.get(cancelToken);

    if (abortController) {
      abortController.abort();
      this.abortControllers.delete(cancelToken);
    }
  };

  public request = async <T = any, E = any>({
    body,
    secure,
    path,
    type,
    query,
    format,
    baseUrl,
    cancelToken,
    ...params
  }: FullRequestParams): Promise<HttpResponse<T, E>> => {
    const secureParams =
      ((typeof secure === "boolean" ? secure : this.baseApiParams.secure) &&
        this.securityWorker &&
        (await this.securityWorker(this.securityData))) ||
      {};
    const requestParams = this.mergeRequestParams(params, secureParams);
    const queryString = query && this.toQueryString(query);
    const payloadFormatter = this.contentFormatters[type || ContentType.Json];
    const responseFormat = format || requestParams.format;

    return this.customFetch(`${baseUrl || this.baseUrl || ""}${path}${queryString ? `?${queryString}` : ""}`, {
      ...requestParams,
      headers: {
        ...(requestParams.headers || {}),
        ...(type && type !== ContentType.FormData ? { "Content-Type": type } : {}),
      },
      signal: (cancelToken ? this.createAbortSignal(cancelToken) : requestParams.signal) || null,
      body: typeof body === "undefined" || body === null ? null : payloadFormatter(body),
    }).then(async (response) => {
      const r = response.clone() as HttpResponse<T, E>;
      r.data = null as unknown as T;
      r.error = null as unknown as E;

      const data = !responseFormat
        ? r
        : await response[responseFormat]()
            .then((data) => {
              if (r.ok) {
                r.data = data;
              } else {
                r.error = data;
              }
              return r;
            })
            .catch((e) => {
              r.error = e;
              return r;
            });

      if (cancelToken) {
        this.abortControllers.delete(cancelToken);
      }

      if (!response.ok) throw data;
      return data;
    });
  };
}

/**
 * @title FastAPI JWT
 * @version 0.1.0
 *
 * fastapi jwt
 */
export class Api<SecurityDataType extends unknown> extends HttpClient<SecurityDataType> {
  auth = {
    /**
     * No description
     *
     * @tags auth
     * @name SetupAuthSetupPost
     * @summary Setup
     * @request POST:/auth/setup
     */
    setupAuthSetupPost: (params: RequestParams = {}) =>
      this.request<any, any>({
        path: `/auth/setup`,
        method: "POST",
        format: "json",
        ...params,
      }),

    /**
     * No description
     *
     * @tags auth
     * @name LoginAuthLoginPost
     * @summary Login
     * @request POST:/auth/login
     */
    loginAuthLoginPost: (data: BodyLoginAuthLoginPost, params: RequestParams = {}) =>
      this.request<any, HTTPValidationError>({
        path: `/auth/login`,
        method: "POST",
        body: data,
        type: ContentType.UrlEncoded,
        format: "json",
        ...params,
      }),
  };
  currentUser = {
    /**
     * No description
     *
     * @tags current_user
     * @name GetMeCurrentUserGet
     * @summary Get Me
     * @request GET:/current_user/
     * @secure
     */
    getMeCurrentUserGet: (params: RequestParams = {}) =>
      this.request<AuthUser, any>({
        path: `/current_user/`,
        method: "GET",
        secure: true,
        format: "json",
        ...params,
      }),
  };
  classroom = {
    /**
     * No description
     *
     * @tags classroom
     * @name GetclassroomClassroomGet
     * @summary Getclassroom
     * @request GET:/classroom/
     * @secure
     */
    getclassroomClassroomGet: (params: RequestParams = {}) =>
      this.request<Classroom[], any>({
        path: `/classroom/`,
        method: "GET",
        secure: true,
        format: "json",
        ...params,
      }),

    /**
     * No description
     *
     * @tags classroom
     * @name CreateclassroomClassroomPost
     * @summary Createclassroom
     * @request POST:/classroom/
     * @secure
     */
    createclassroomClassroomPost: (data: ClassroomCreate, params: RequestParams = {}) =>
      this.request<Classroom, HTTPValidationError>({
        path: `/classroom/`,
        method: "POST",
        body: data,
        secure: true,
        type: ContentType.Json,
        format: "json",
        ...params,
      }),

    /**
     * No description
     *
     * @tags classroom
     * @name GetclassroomIdClassroomIdGet
     * @summary Getclassroomid
     * @request GET:/classroom/{ID}
     * @secure
     */
    getclassroomIdClassroomIdGet: (
      id: string,
      query: {
        /** Id */
        id: number;
      },
      params: RequestParams = {},
    ) =>
      this.request<Classroom, HTTPValidationError>({
        path: `/classroom/${id}`,
        method: "GET",
        query: query,
        secure: true,
        format: "json",
        ...params,
      }),

    /**
     * No description
     *
     * @tags classroom
     * @name UpdateclassroomClassroomIdUpdatePatch
     * @summary Updateclassroom
     * @request PATCH:/classroom/{id}/update
     * @secure
     */
    updateclassroomClassroomIdUpdatePatch: (id: number, data: ClassroomUpdate, params: RequestParams = {}) =>
      this.request<Classroom, HTTPValidationError>({
        path: `/classroom/${id}/update`,
        method: "PATCH",
        body: data,
        secure: true,
        type: ContentType.Json,
        format: "json",
        ...params,
      }),

    /**
     * No description
     *
     * @tags classroom
     * @name DeleteclassroomClassroomIdDeleteDelete
     * @summary Deleteclassroom
     * @request DELETE:/classroom/{id}/delete
     * @secure
     */
    deleteclassroomClassroomIdDeleteDelete: (id: number, params: RequestParams = {}) =>
      this.request<any, HTTPValidationError>({
        path: `/classroom/${id}/delete`,
        method: "DELETE",
        secure: true,
        format: "json",
        ...params,
      }),
  };
  course = {
    /**
     * No description
     *
     * @tags course
     * @name GetcourseCourseGet
     * @summary Getcourse
     * @request GET:/course/
     * @secure
     */
    getcourseCourseGet: (params: RequestParams = {}) =>
      this.request<Course[], any>({
        path: `/course/`,
        method: "GET",
        secure: true,
        format: "json",
        ...params,
      }),

    /**
     * No description
     *
     * @tags course
     * @name CreatecourseCoursePost
     * @summary Createcourse
     * @request POST:/course/
     * @secure
     */
    createcourseCoursePost: (data: CourseCreate, params: RequestParams = {}) =>
      this.request<Course, HTTPValidationError>({
        path: `/course/`,
        method: "POST",
        body: data,
        secure: true,
        type: ContentType.Json,
        format: "json",
        ...params,
      }),

    /**
     * No description
     *
     * @tags course
     * @name GetcourseidCourseIdGet
     * @summary Getcourseid
     * @request GET:/course/{id}
     * @secure
     */
    getcourseidCourseIdGet: (id: number, params: RequestParams = {}) =>
      this.request<Course, HTTPValidationError>({
        path: `/course/${id}`,
        method: "GET",
        secure: true,
        format: "json",
        ...params,
      }),

    /**
     * No description
     *
     * @tags course
     * @name UpdatecourseCourseIdUpdatePatch
     * @summary Updatecourse
     * @request PATCH:/course/{id}/update
     * @secure
     */
    updatecourseCourseIdUpdatePatch: (id: number, data: CourseUpdate, params: RequestParams = {}) =>
      this.request<Course, HTTPValidationError>({
        path: `/course/${id}/update`,
        method: "PATCH",
        body: data,
        secure: true,
        type: ContentType.Json,
        format: "json",
        ...params,
      }),

    /**
     * No description
     *
     * @tags course
     * @name UpdatecourseCourseIdDeleteDelete
     * @summary Updatecourse
     * @request DELETE:/course/{id}/delete
     * @secure
     */
    updatecourseCourseIdDeleteDelete: (id: number, params: RequestParams = {}) =>
      this.request<any, HTTPValidationError>({
        path: `/course/${id}/delete`,
        method: "DELETE",
        secure: true,
        format: "json",
        ...params,
      }),
  };
  user = {
    /**
     * No description
     *
     * @tags user
     * @name GetuserUserGet
     * @summary Getuser
     * @request GET:/user/
     * @secure
     */
    getuserUserGet: (params: RequestParams = {}) =>
      this.request<Account[], any>({
        path: `/user/`,
        method: "GET",
        secure: true,
        format: "json",
        ...params,
      }),

    /**
     * No description
     *
     * @tags user
     * @name CreateUserUserPost
     * @summary Create User
     * @request POST:/user/
     * @secure
     */
    createUserUserPost: (data: AccountCreate, params: RequestParams = {}) =>
      this.request<Account, HTTPValidationError>({
        path: `/user/`,
        method: "POST",
        body: data,
        secure: true,
        type: ContentType.Json,
        format: "json",
        ...params,
      }),

    /**
     * No description
     *
     * @tags user
     * @name GetteacherUserTeacherGet
     * @summary Getteacher
     * @request GET:/user/teacher
     * @secure
     */
    getteacherUserTeacherGet: (params: RequestParams = {}) =>
      this.request<UserSelected[], any>({
        path: `/user/teacher`,
        method: "GET",
        secure: true,
        format: "json",
        ...params,
      }),

    /**
     * No description
     *
     * @tags user
     * @name GetteacherUserStudentGet
     * @summary Getteacher
     * @request GET:/user/student
     * @secure
     */
    getteacherUserStudentGet: (params: RequestParams = {}) =>
      this.request<UserSelected[], any>({
        path: `/user/student`,
        method: "GET",
        secure: true,
        format: "json",
        ...params,
      }),

    /**
     * No description
     *
     * @tags user
     * @name GetuserIdUserIdGet
     * @summary Getuser Id
     * @request GET:/user/{id}
     * @secure
     */
    getuserIdUserIdGet: (id: number, params: RequestParams = {}) =>
      this.request<Account, HTTPValidationError>({
        path: `/user/${id}`,
        method: "GET",
        secure: true,
        format: "json",
        ...params,
      }),

    /**
     * No description
     *
     * @tags user
     * @name UpdateUserUserIdUpdatePatch
     * @summary Update User
     * @request PATCH:/user/{id}/update
     * @secure
     */
    updateUserUserIdUpdatePatch: (id: number, data: AccountUpdate, params: RequestParams = {}) =>
      this.request<Account, HTTPValidationError>({
        path: `/user/${id}/update`,
        method: "PATCH",
        body: data,
        secure: true,
        type: ContentType.Json,
        format: "json",
        ...params,
      }),

    /**
     * No description
     *
     * @tags user
     * @name DeactivateUserUserIdDeactivatePost
     * @summary Deactivate User
     * @request POST:/user/{id}/deactivate
     * @secure
     */
    deactivateUserUserIdDeactivatePost: (id: number, params: RequestParams = {}) =>
      this.request<Account, HTTPValidationError>({
        path: `/user/${id}/deactivate`,
        method: "POST",
        secure: true,
        format: "json",
        ...params,
      }),

    /**
     * No description
     *
     * @tags user
     * @name ActivateUserUserIdActivatePost
     * @summary Activate User
     * @request POST:/user/{id}/activate
     * @secure
     */
    activateUserUserIdActivatePost: (id: number, params: RequestParams = {}) =>
      this.request<Account, HTTPValidationError>({
        path: `/user/${id}/activate`,
        method: "POST",
        secure: true,
        format: "json",
        ...params,
      }),
  };
  role = {
    /**
     * No description
     *
     * @tags role
     * @name GetroleRoleGet
     * @summary Getrole
     * @request GET:/role/
     * @secure
     */
    getroleRoleGet: (params: RequestParams = {}) =>
      this.request<Role[], any>({
        path: `/role/`,
        method: "GET",
        secure: true,
        format: "json",
        ...params,
      }),
  };
  department = {
    /**
     * No description
     *
     * @tags department
     * @name GetdepartmentDepartmentGet
     * @summary Getdepartment
     * @request GET:/department/
     * @secure
     */
    getdepartmentDepartmentGet: (params: RequestParams = {}) =>
      this.request<Department[], any>({
        path: `/department/`,
        method: "GET",
        secure: true,
        format: "json",
        ...params,
      }),

    /**
     * No description
     *
     * @tags department
     * @name CreatedepartmentDepartmentPost
     * @summary Createdepartment
     * @request POST:/department/
     * @secure
     */
    createdepartmentDepartmentPost: (data: DepartmentCreate, params: RequestParams = {}) =>
      this.request<Department, HTTPValidationError>({
        path: `/department/`,
        method: "POST",
        body: data,
        secure: true,
        type: ContentType.Json,
        format: "json",
        ...params,
      }),

    /**
     * No description
     *
     * @tags department
     * @name GetdepartmentidDepartmentIdGet
     * @summary Getdepartmentid
     * @request GET:/department/{id}
     * @secure
     */
    getdepartmentidDepartmentIdGet: (id: number, params: RequestParams = {}) =>
      this.request<Department, HTTPValidationError>({
        path: `/department/${id}`,
        method: "GET",
        secure: true,
        format: "json",
        ...params,
      }),

    /**
     * No description
     *
     * @tags department
     * @name UpdatedepartmentDepartmentIdUpdatePatch
     * @summary Updatedepartment
     * @request PATCH:/department/{id}/update
     * @secure
     */
    updatedepartmentDepartmentIdUpdatePatch: (id: number, data: DepartmentUpdate, params: RequestParams = {}) =>
      this.request<Department, HTTPValidationError>({
        path: `/department/${id}/update`,
        method: "PATCH",
        body: data,
        secure: true,
        type: ContentType.Json,
        format: "json",
        ...params,
      }),

    /**
     * No description
     *
     * @tags department
     * @name DeletedepartmentDepartmentIdDeleteDelete
     * @summary Deletedepartment
     * @request DELETE:/department/{id}/delete
     * @secure
     */
    deletedepartmentDepartmentIdDeleteDelete: (id: number, params: RequestParams = {}) =>
      this.request<any, HTTPValidationError>({
        path: `/department/${id}/delete`,
        method: "DELETE",
        secure: true,
        format: "json",
        ...params,
      }),
  };
  major = {
    /**
     * No description
     *
     * @tags major
     * @name GetmajorMajorGet
     * @summary Getmajor
     * @request GET:/major/
     * @secure
     */
    getmajorMajorGet: (params: RequestParams = {}) =>
      this.request<Major[], any>({
        path: `/major/`,
        method: "GET",
        secure: true,
        format: "json",
        ...params,
      }),

    /**
     * No description
     *
     * @tags major
     * @name CreatemajorMajorPost
     * @summary Createmajor
     * @request POST:/major/
     * @secure
     */
    createmajorMajorPost: (data: MajorCreate, params: RequestParams = {}) =>
      this.request<Major, HTTPValidationError>({
        path: `/major/`,
        method: "POST",
        body: data,
        secure: true,
        type: ContentType.Json,
        format: "json",
        ...params,
      }),

    /**
     * No description
     *
     * @tags major
     * @name GetmajoridMajorIdGet
     * @summary Getmajorid
     * @request GET:/major/{id}
     * @secure
     */
    getmajoridMajorIdGet: (id: number, params: RequestParams = {}) =>
      this.request<Major, HTTPValidationError>({
        path: `/major/${id}`,
        method: "GET",
        secure: true,
        format: "json",
        ...params,
      }),

    /**
     * No description
     *
     * @tags major
     * @name UpdatemajorMajorIdUpdatePatch
     * @summary Updatemajor
     * @request PATCH:/major/{id}/update
     * @secure
     */
    updatemajorMajorIdUpdatePatch: (id: number, data: MajorUpdate, params: RequestParams = {}) =>
      this.request<Major, HTTPValidationError>({
        path: `/major/${id}/update`,
        method: "PATCH",
        body: data,
        secure: true,
        type: ContentType.Json,
        format: "json",
        ...params,
      }),

    /**
     * No description
     *
     * @tags major
     * @name DeletemajorMajorIdDeleteDelete
     * @summary Deletemajor
     * @request DELETE:/major/{id}/delete
     * @secure
     */
    deletemajorMajorIdDeleteDelete: (id: number, params: RequestParams = {}) =>
      this.request<any, HTTPValidationError>({
        path: `/major/${id}/delete`,
        method: "DELETE",
        secure: true,
        format: "json",
        ...params,
      }),
  };
  semester = {
    /**
     * No description
     *
     * @tags semester
     * @name GetsemesterSemesterGet
     * @summary Getsemester
     * @request GET:/semester/
     * @secure
     */
    getsemesterSemesterGet: (params: RequestParams = {}) =>
      this.request<Semester[], any>({
        path: `/semester/`,
        method: "GET",
        secure: true,
        format: "json",
        ...params,
      }),

    /**
     * No description
     *
     * @tags semester
     * @name CreatemajorSemesterPost
     * @summary Createmajor
     * @request POST:/semester/
     * @secure
     */
    createmajorSemesterPost: (data: SemesterCreate, params: RequestParams = {}) =>
      this.request<Semester, HTTPValidationError>({
        path: `/semester/`,
        method: "POST",
        body: data,
        secure: true,
        type: ContentType.Json,
        format: "json",
        ...params,
      }),

    /**
     * No description
     *
     * @tags semester
     * @name GetsemesteridSemesterIdGet
     * @summary Getsemesterid
     * @request GET:/semester/{id}
     * @secure
     */
    getsemesteridSemesterIdGet: (id: number, params: RequestParams = {}) =>
      this.request<Semester, HTTPValidationError>({
        path: `/semester/${id}`,
        method: "GET",
        secure: true,
        format: "json",
        ...params,
      }),

    /**
     * No description
     *
     * @tags semester
     * @name UpdatesemesterSemesterIdUpdatePatch
     * @summary Updatesemester
     * @request PATCH:/semester/{id}/update
     * @secure
     */
    updatesemesterSemesterIdUpdatePatch: (id: number, data: SemesterUpdate, params: RequestParams = {}) =>
      this.request<Semester, HTTPValidationError>({
        path: `/semester/${id}/update`,
        method: "PATCH",
        body: data,
        secure: true,
        type: ContentType.Json,
        format: "json",
        ...params,
      }),

    /**
     * No description
     *
     * @tags semester
     * @name DeletesemesterSemesterIdDeleteDelete
     * @summary Deletesemester
     * @request DELETE:/semester/{id}/delete
     * @secure
     */
    deletesemesterSemesterIdDeleteDelete: (id: number, params: RequestParams = {}) =>
      this.request<any, HTTPValidationError>({
        path: `/semester/${id}/delete`,
        method: "DELETE",
        secure: true,
        format: "json",
        ...params,
      }),
  };
  opencourse = {
    /**
     * No description
     *
     * @tags opencourse
     * @name GetopencourseOpencourseGet
     * @summary Getopencourse
     * @request GET:/opencourse/
     * @secure
     */
    getopencourseOpencourseGet: (params: RequestParams = {}) =>
      this.request<Opencourse[], any>({
        path: `/opencourse/`,
        method: "GET",
        secure: true,
        format: "json",
        ...params,
      }),

    /**
     * No description
     *
     * @tags opencourse
     * @name CreateopencourseOpencoursePost
     * @summary Createopencourse
     * @request POST:/opencourse/
     * @secure
     */
    createopencourseOpencoursePost: (data: OpencourseCreate, params: RequestParams = {}) =>
      this.request<Opencourse, HTTPValidationError>({
        path: `/opencourse/`,
        method: "POST",
        body: data,
        secure: true,
        type: ContentType.Json,
        format: "json",
        ...params,
      }),

    /**
     * No description
     *
     * @tags opencourse
     * @name GetopencourseOpenOpencourseOpenGet
     * @summary Getopencourse Open
     * @request GET:/opencourse/open
     * @secure
     */
    getopencourseOpenOpencourseOpenGet: (params: RequestParams = {}) =>
      this.request<Opencourse[], any>({
        path: `/opencourse/open`,
        method: "GET",
        secure: true,
        format: "json",
        ...params,
      }),

    /**
     * No description
     *
     * @tags opencourse
     * @name GetopencourseidOpencourseIdGet
     * @summary Getopencourseid
     * @request GET:/opencourse/{id}
     * @secure
     */
    getopencourseidOpencourseIdGet: (id: number, params: RequestParams = {}) =>
      this.request<Opencourse, HTTPValidationError>({
        path: `/opencourse/${id}`,
        method: "GET",
        secure: true,
        format: "json",
        ...params,
      }),

    /**
     * No description
     *
     * @tags opencourse
     * @name UpdateopencourseOpencourseIdUpdatePatch
     * @summary Updateopencourse
     * @request PATCH:/opencourse/{id}/update
     * @secure
     */
    updateopencourseOpencourseIdUpdatePatch: (id: number, data: OpencourseUpdate, params: RequestParams = {}) =>
      this.request<Opencourse, HTTPValidationError>({
        path: `/opencourse/${id}/update`,
        method: "PATCH",
        body: data,
        secure: true,
        type: ContentType.Json,
        format: "json",
        ...params,
      }),

    /**
     * No description
     *
     * @tags opencourse
     * @name DeleteopencourseOpencourseIdDeleteDelete
     * @summary Deleteopencourse
     * @request DELETE:/opencourse/{id}/delete
     * @secure
     */
    deleteopencourseOpencourseIdDeleteDelete: (id: number, params: RequestParams = {}) =>
      this.request<any, HTTPValidationError>({
        path: `/opencourse/${id}/delete`,
        method: "DELETE",
        secure: true,
        format: "json",
        ...params,
      }),
  };
  enrollment = {
    /**
     * No description
     *
     * @tags enrollment
     * @name GetenrollmentEnrollmentGet
     * @summary Getenrollment
     * @request GET:/enrollment/
     * @secure
     */
    getenrollmentEnrollmentGet: (params: RequestParams = {}) =>
      this.request<Enrollment[], any>({
        path: `/enrollment/`,
        method: "GET",
        secure: true,
        format: "json",
        ...params,
      }),

    /**
     * No description
     *
     * @tags enrollment
     * @name RegisterenrollmentEnrollmentPost
     * @summary Registerenrollment
     * @request POST:/enrollment/
     * @secure
     */
    registerenrollmentEnrollmentPost: (data: EnrollmentCreate, params: RequestParams = {}) =>
      this.request<Enrollment, HTTPValidationError>({
        path: `/enrollment/`,
        method: "POST",
        body: data,
        secure: true,
        type: ContentType.Json,
        format: "json",
        ...params,
      }),

    /**
     * No description
     *
     * @tags enrollment
     * @name GetenrollmentidEnrollmentIdGet
     * @summary Getenrollmentid
     * @request GET:/enrollment/{id}
     * @secure
     */
    getenrollmentidEnrollmentIdGet: (id: number, params: RequestParams = {}) =>
      this.request<Enrollment, HTTPValidationError>({
        path: `/enrollment/${id}`,
        method: "GET",
        secure: true,
        format: "json",
        ...params,
      }),

    /**
     * No description
     *
     * @tags enrollment
     * @name UpdateenrollmentEnrollmentIdUpdatePatch
     * @summary Updateenrollment
     * @request PATCH:/enrollment/{id}/update
     * @secure
     */
    updateenrollmentEnrollmentIdUpdatePatch: (id: number, data: EnrollmentUpdate, params: RequestParams = {}) =>
      this.request<Enrollment, HTTPValidationError>({
        path: `/enrollment/${id}/update`,
        method: "PATCH",
        body: data,
        secure: true,
        type: ContentType.Json,
        format: "json",
        ...params,
      }),

    /**
     * No description
     *
     * @tags enrollment
     * @name DeleteenrollmentEnrollmentIdDeleteDelete
     * @summary Deleteenrollment
     * @request DELETE:/enrollment/{id}/delete
     * @secure
     */
    deleteenrollmentEnrollmentIdDeleteDelete: (id: number, params: RequestParams = {}) =>
      this.request<any, HTTPValidationError>({
        path: `/enrollment/${id}/delete`,
        method: "DELETE",
        secure: true,
        format: "json",
        ...params,
      }),
  };
}
